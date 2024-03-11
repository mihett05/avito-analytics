import React from 'react';
import { List, Datagrid, TextField } from 'react-admin';

export const PricesList = () => (
  <List>
    <Datagrid rowClick="edit">
      <TextField source="id" />
      <TextField source="location_id" />
      <TextField source="category_id" />
      <TextField source="price" />
    </Datagrid>
  </List>
);

export default PricesList;
