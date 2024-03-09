import React from 'react';
import { Admin, Resource } from 'react-admin';
import jsonServerProvider from 'ra-data-json-server';

import LocationsList from '~/resources/locations/list';

const dataProvider = jsonServerProvider('https://jsonplaceholder.typicode.com');

function App() {
  return (
    <Admin dataProvider={dataProvider}>
      <Resource name="locations" list={LocationsList} />
    </Admin>
  );
}

export default App;
