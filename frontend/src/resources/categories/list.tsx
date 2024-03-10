import React from 'react';
import { List, Datagrid, TextField } from 'react-admin'

export const CategoriesList = () => (
  <List>
      <Datagrid rowClick="edit">
          <TextField source="id" />
          <TextField source="name" />
          <TextField source="parent_id" />
          <TextField source="key" />
      </Datagrid>
  </List>
);

export default CategoriesList;