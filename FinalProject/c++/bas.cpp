#include <bits/stdc++.h>
#include <vector>
#include <unordered_map>
#include <string>
using namespace std;
const int N=30000+5;
int n, A, B;
char c[N];
int a[N],b[N],d[N],st[N*4];
const long long P=1000000009;
long long has[N],pr[N];

void input(){
    memset(c,0,sizeof(c));
    memset(a,0,sizeof(a));
    memset(b,0,sizeof(b));
    memset(d,0,sizeof(d));
    memset(st,0,sizeof(st));
    memset(has,0,sizeof(has));
    memset(pr,0,sizeof(pr));
    scanf("%d %d %d",&n,&A,&B);
    scanf("%s",c+1);
}
inline bool ch(int x,int y,int z){
    return ( has[x+z-1] - has[x-1]+P) * pr[n-x] % P == (has[y+z-1] - has[y-1] + P) * pr[n-y] % P;
}
inline bool boo(int x, int y){
    int r = n - max(x,y) + 2;
    if (ch(x,y,r-1)) return x>y;
    int m,l=0;
    while (l+1<r){
        m=(l+r)/2;
        if (ch(x,y,m))  l=m;
        else            r=m;
    }
    return c[x+l]<c[y+l];
}
void build(int l,int r,int x){
    if (l+1==r){
        st[x]=a[l];
        return;
    }
    build(l,(l+r)/2,x*2);
    build((l+r)/2,r,x*2+1);
    st[x]=min(st[x*2],st[x*2+1]);
}
int get(int l,int r,int x,int L,int R){
    if (L<=l && r-1<=R) return st[x];
    if (r-1<L || R<l) return n+5;
    return min(get(l,(l+r)/2,x*2,L,R),get((l+r)/2,r,x*2+1,L,R));
}
void sol(){
    pr[0]=1;
    c[n+1]=0;
    for (int i=1;i<=n+1;i++) pr[i]=pr[i-1]*349%P;
    for (int i=1;i<=n+1;i++) has[i]=(has[i-1]+pr[i]*c[i])%P;
    for (int i=1;i<=n;i++) a[i]=i;
    sort(a+1,a+n+1,boo);
    for (int i=1;i<=n;i++) b[a[i]]=i;
    build(1,n+1,1);
    d[0]=0;
    for (int i=1;i<=n;i++){
        d[i]=d[i-1]+A;
        int l=0;
        int r=i/2+1;
        while (l+1<r){
            int m=(l+r)/2;
            int ll=1;
            int mm,rr=b[i-m+1];
            while (ll<rr){
                mm=(ll+rr)/2;
                if (ch(a[mm],i-m+1,m))  rr=mm;
                else                    ll=mm+1;
            }
            int L=ll;
            ll=b[i-m+1];
            rr=n+1;
            while (ll+1<rr){
                mm=(ll+rr)/2;
                if (ch(a[mm],i-m+1,m))   ll=mm;
                else                     rr=mm;
            }
            int R=ll;
            if (get(1,n+1,1,L,R)<=i-m*2+1)  l=m;
            else                            r=m;
        }
        d[i]=min(d[i],d[i-l]+B);
    }
    cout<<d[n]<<endl;
}
int main() {
    int test;
    scanf("%d",&test);
    while (test--){
        input();
        sol();
    }
    return 0;
}