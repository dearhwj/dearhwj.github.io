---
layout: post
title:  Mockito使用Tips
category: JAVA
keywords: Mockito
---
## 收集
### Mockito 如何 mock 返回值为 void 的方法
[Mockito 如何 mock 返回值为 void 的方法](https://yanbin.blog/mockito-how-to-mock-void-method/)

一般不用对 void 方法打桩, 事后 verify 就行

```
@Test
public void shouldCallUserDaoSaveMethod() {
  UserDao userDao = Mockito.mock(UserDao.class);
  UserService userService = new UserService(userDao);
  
  User user = new User(1, "Yanbin");
  userService.saveUser(user);
 
  verify(userDao, times(1)).save(user);
}
```
模拟 void 方法抛出异常时调用者的响应

```

@Test(expected = ApplicationException.class)
public void raiseApplicationExceptionIfDataAccessExceptionOccursFromUserDao() {
  UserDao userDao = Mockito.mock(UserDao.class);
  UserService userService = new UserService(userDao);
  User user = new User(1, "Yanbin");
 
  doThrow(new DataAccessException()).when(userDao).save(user);
 
  userService.saveUser(user);
}

```