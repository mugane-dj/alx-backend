// Cache products with redis client
import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const client = createClient();

client.on("connect", function() {
  console.log('Redis client connected to the server');
});

client.on("error", function(err) {
  if (err.code === 'ECONNREFUSED') {
    console.log(`Redis client not connected to the server: ${err}`);
  } else {
    throw err;
  }
});

const listProducts = [
  {id: 1, name: 'Suitcase 250', price: 50, stock: 4},
  {id: 2, name: 'Suitcase 450', price: 100, stock: 10},
  {id: 3, name: 'Suitcase 650', price: 350, stock: 2},
  {id: 4, name: 'Suitcase 1050', price: 550, stock: 5},
]

const getItemById = (id) => {
 for (const item of listProducts) {
   if (item.id === id) {
     return item;
   }
 }
}

const reserveStockById = (itemId, stock) => {
  client.set(itemId, stock);
}

const getAsync = promisify(client.get).bind(client);

const getCurrentReservedStockById = async(itemId) => {
  const itemStock = await getAsync(itemId);
  return itemStock;
}

app.get('/list_products', (req, res) => {
  const formattedProducts = listProducts.map(item => ({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock
  }));
  res.json(formattedProducts);
});

app.get('/list_products/:itemId', (req, res) => {
  const id = parseInt(req.params.itemId);
  const item = getItemById(id);
  if (!item) {
    res.json({'status':'Product not found'});
  } else {
   const reservedStock = getCurrentReservedStockById(item.id);
   res.json({
     itemId: item.id,
     itemName: item.name,
     price: item.price,
     initialAvailableQuantity: item.stock,
     currentQuantity: reservedStock,
   });
  }
});

app.listen(1245);
