# def permute(n):
#
#   if n==len(a):
#     print(a)
#     return
#
#   for i in range(n,len(a)):
#     swap(i,n)
#     permute(n+1)
#     swap(i,n)


def swap(a, x, y):
  a[x],a[y]=a[y],a[x]

a=[1,2,3,4,5]
print(swap(a,1,3))
print(a[1])
print(a[3])
print(a)
# permute(0)
#
# def permute(n):
#
#   if n==len(a):
#     print(a)
#     return
#
#   for i in range(n,len(a)):
#     swap(a[i],a[n])
#     permute(n+1)
#     swap(a[i],a[n])
#
# # def swap(x,y):
# #   x,y=y,x
#
# a=[1,2,3,4]
# permute(0)