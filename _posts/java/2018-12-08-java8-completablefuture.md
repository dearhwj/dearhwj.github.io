CompletableFuture



public Future<Double> getPriceAsync(String product) {
CompletableFuture<Double> futurePrice = new CompletableFuture<>();
new Thread( () -> { 11
  如果价格计算正常结 束，完成Future操作 并设置商品价格
try {
    double price = calculatePrice(product);
    futurePrice.complete(price);
} catch (Exception ex) {
    futurePrice.completeExceptionally(ex);
12
    }
}
}).start(); 13 return futurePrice;



使用工厂方法supplyAsync创建CompletableFuture****