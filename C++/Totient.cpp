#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;
const int MAXN = 5e5 + 5;

long long modpow(long long a, long long b) {
  long long res = 1;
  while (b) {
    if (b&1)
      res = (res * a) % MOD;
    a = (a * a) % MOD;
    b >>= 1;
  }
  return res;
}

long long f[MAXN];
long long invf[MAXN];

long long ncr(long long n, long long r) {
  if (r == 0 || n == r) return 1;
  return (((f[n] * invf[n-r]) % MOD) * invf[r]) % MOD;
}

int main() {
  
  f[0] = 1;
  for (int i = 1; i < MAXN; i++) {
    f[i] = (f[i-1] * i) % MOD;
    invf[i] = modpow(f[i], MOD-2);
  }
  
  
  cout<<invf[2];
  
  int tt;
  cin >> tt;
  while (tt--) {
    long long m, n, k;
    cin >> m >> n >> k;
    cout << (ncr(m, k) * modpow(2, n) ) % MOD << '\n';
  }
  
}
