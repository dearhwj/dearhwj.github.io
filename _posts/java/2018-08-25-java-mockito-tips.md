---
layout: post
title:  JAVA单元测试之Mock
category: JAVA
keywords: Mockito, PowerMockito
---
## 收集

### Mock Final Classes and Methods with Mockito
原文地址:[https://www.baeldung.com/mockito-final](https://www.baeldung.com/mockito-final)

很诡异的地方要在src/test/resources/mockito-extensions下放一个文件org.mockito.plugins.MockMaker 
还有在里面加入一行

```
mock-maker-inline
```

### 使用PowerMockito 对静态类进行mock
原文地址:[https://www.cnblogs.com/lianshan/p/6930771.html](https://www.cnblogs.com/lianshan/p/6930771.html)

```
@RunWith(PowerMockRunner.class)  //1.
@PrepareForTest({LogUtil.class}) //2.
public class AddressBookServiceTest_mock {
 
 
    @Before
    public void setUp() {
        MockitoAnnotations.initMocks(this);
    }
 　 @Test
    public void test_staticMethod_PowerMock()  {
        //绕过静态类
        PowerMockito.mockStatic(LogUtil.class);//3.绕过静态类
        when(LogUtil.getLogBean(json)).thenReturn(new SensitiveInfoOperationLog());//4.预设静态类返回值
        String response = addressBookServiceImpl.queryAddressBookFuzzy(json);
    }
}

```

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