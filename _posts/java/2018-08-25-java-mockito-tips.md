---
layout: post
title:  Mockito使用Tips
category: JAVA
keywords: Mockito
---
## 收集

### java.lang.NoSuchMethodError: org.hamcrest.Matcher.describeMismatch处理

原因：是mockito把hamcrest相关的Matcher都打到自己的包里面，class加载的时候把mockito的优先加载进去了，导致新版本的hamcrest的类无法被加载引用。
解决方案：在类加载的时候要提前加载hamcrest自己的类，在ide里面可以通过调整maven依赖的顺序。也就是把hamcrest依赖写在mockito依赖的前面。

```
 <dependency>
    <groupId>org.hamcrest</groupId>
    <artifactId>hamcrest-all</artifactId>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.mockito</groupId>
    <artifactId>mockito-all</artifactId>
    <scope>test</scope>
</dependency>
        
```        

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