import React from 'react';
import { List, Datagrid, TextField } from 'react-admin';

export const LocationsList = () => (
  <List>
    <Datagrid rowClick="show">
      <TextField source="id" />
      <TextField source="name" />
      <TextField source="parent_id" />
      <TextField source="key" />
    </Datagrid>
  </List>
);

export default LocationsList;
