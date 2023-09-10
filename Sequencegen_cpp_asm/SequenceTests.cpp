/*
 * Yves Roggeman &  Jacopo De Stefani - 2018/03
 * Main test program / call assembler function (-m32)
 *
 */

#include <cstddef>            // nullptr_t, ptrdiff_t, size_t
#include <iostream>           // cin, cout...
#include <ostream>            // output stream definition
#include <cstring>

extern "C" bool validate_sequence(char message[], unsigned sequence);

std::ostream& printhex(std::ostream&, unsigned);
void test(char*, unsigned);

int main () {
  const unsigned short lg = 256;
  char msg[lg];
  unsigned hash = 42;

  std::cout << "Message : "; std::cin >> msg;
  std::cout << "Hachage : "; std::cin >> hash;
  test(msg, hash);

  std::strcpy(msg, "00001");
  hash = 0x037DE427; // OK for "00001"
  test(msg, hash);

  std::strcpy(msg, "1234432");
  hash = 0x1F646EB7; // OK for "1234432"
  test(msg, hash);

  std::strcpy(msg, "1415926535");
  hash = 0;          // KO for decimals of PI
  test(msg, hash);

  std::strcpy(msg, "");
  hash = 0x0F155778; // OK for empty string
  test(msg, hash);

  return 0;
}

// Auxiliary function for testing
void test(char* msg, unsigned hash){
  std::cout << "Message:" << '"' << msg << '"' << std::endl;
  std::cout << "Hash:" ;
  printhex(std::cout, hash);
  std::cout << std::endl;
  std::cout << (validate_sequence(msg, hash) ? "OK" : "KO") << std::endl;}


// Output unsigned in hexadecimal format
std::ostream& printhex(std::ostream& out, unsigned x) {
  out << "0x";
  const std::ios_base::fmtflags flags
    = out.setf(std::ios_base::hex, std::ios_base::basefield);
  const char filler = out.fill('0');
  out.width(8); out << x;
  out.fill(filler); out.flags(flags);
  return out;
}

extern "C" unsigned project (unsigned checksum) {
  unsigned tmp = checksum;
  // tmp = checksum mod 216+1 (a Fermat prime); O codes 226
  tmp = (tmp & 0xFFFF) - (tmp>>16 & 0xFFFF);
  if (tmp & 0xFFFF0000) ++tmp; // carry
  tmp &= 0xFFFF;
  // add-multiply (by PI decimals)
  tmp += 0x6A88;
  tmp *= 0x243F;
  return tmp ^ checksum; }

