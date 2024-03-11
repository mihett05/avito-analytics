import React from 'react';
import { List, Datagrid, TextField } from 'react-admin'

export const PricesList = () => (
  <List>
      <Datagrid rowClick="edit">
          <TextField source="price" />
          <TextField source="matrix_id" />
          <TextField source="location_id" />
          <TextField source="category_id" />
      </Datagrid>
  </List>
);

export default PricesList;