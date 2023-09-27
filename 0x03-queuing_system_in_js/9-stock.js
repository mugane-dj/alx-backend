// Cache products with redis client
import express from 'express';
import { createClient, print } from 'redis';
import { promisify } from 'util';

const PORT = 1245;
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
  client.set(itemId, stock, print);
}

const getAsync = promisify(client.get).bind(client);

const getCurrentReservedStockById = async (itemId) => {
  try {
    const itemStock = await getAsync(itemId);
    return itemStock;
  } catch (error) {
    console.error(error);
  }
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

app.get('/list_products/:itemId', async (req, res) => {
  const id = parseInt(req.params.itemId);
  const item = getItemById(id);
  if (!item) {
    res.json({'status':'Product not found'});
  } else {
   const reservedStock = await getCurrentReservedStockById(id);
   res.json({
     itemId: item.id,
     itemName: item.name,
     price: item.price,
     initialAvailableQuantity: item.stock,
     currentQuantity: reservedStock,
   });
  }
});

app.get('/reserve_product/:itemId', (req, res) => {
  const id = parseInt(req.params.itemId);
  const item = getItemById(id);
  if (!item) {
    res.json({'status':'Product not found'});
  } else if (item.stock < 1) {
    res.json({'status': 'Not enough stock available', 'itemId': item.id});
  } else {
    reserveStockById(item.id, 1);
    res.json({'status': 'Reservation confirmed', 'itemId': item.id});
  }
});

app.listen(PORT, () => {
  console.log(`Server running on port: ${PORT}`)
});
