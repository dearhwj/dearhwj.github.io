---
layout: post
title: Junit Tips
category: JAVA
keywords: deprecated
---

## 如何运行多个Runner
原文[https://stackoverflow.com/questions/24431427/multiple-runwith-statements-in-junit](https://stackoverflow.com/questions/24431427/multiple-runwith-statements-in-junit）

没辙只能运行一个，办法就是用其中一个，另外一个在TEST的before中调用相应的方法进行初始化

```

@RunWith(PandoraBootRunner.class)
public class ProdPlanRunnableBuilderTest extends  RhinoBaseTest {


    @Before
    public void setUp() {
        MockitoAnnotations.initMocks(this);
    }
    
}

```    
    

