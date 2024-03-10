import React from 'react';
import { Admin, EditGuesser, Resource, ShowGuesser } from 'react-admin';
import jsonServerProvider from 'ra-data-json-server';
import LocationsList from '../resources/locations/list'
import CategoriesList from '~/resources/categories/list';
import PricesList from '~/resources/prices/list';
import MatriciesList from '~/resources/matricies/list';

const dataProvider = jsonServerProvider('http://localhost:4200'); // На нём бд была развернута :)

function App() {
  return (
    <Admin dataProvider={dataProvider}>
      <Resource name="locations" list={ LocationsList } edit={ EditGuesser } show={ ShowGuesser } />
      <Resource name="categories" list={ CategoriesList } edit={ EditGuesser } show={ ShowGuesser } />
      <Resource name="prices" list={ PricesList } edit={ EditGuesser } show={ ShowGuesser } />
      <Resource name="matricies" list={ MatriciesList } edit={ EditGuesser } show={ ShowGuesser } />
    </Admin>
  );
}

export default App;