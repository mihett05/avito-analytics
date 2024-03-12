import React from 'react';
import { Admin, EditGuesser, Resource, ShowGuesser } from 'react-admin';
import { dataProvider } from '~/providers';

import LocationsList from '../resources/locations/list';
import CategoriesList from '~/resources/categories/list';
import PricesList from '~/resources/prices/list';
import MatriciesList from '~/resources/matricies/list';
import LocationsEdit from '~/resources/locations/edit';
import CategoriesEdit from '~/resources/categories/edit';
import LocationsShow from '~/resources/locations/show';
import CategoriesShow from '~/resources/categories/show';

function App() {
  return (
    <Admin dataProvider={dataProvider}>
      <Resource name="location" list={LocationsList} edit={LocationsEdit} show={LocationsShow} />
      <Resource name="category" list={CategoriesList} edit={CategoriesEdit} show={CategoriesShow} />
      <Resource name="price" list={PricesList} edit={EditGuesser} show={ShowGuesser} />
      <Resource name="matrix" list={MatriciesList} edit={EditGuesser} show={ShowGuesser} />
    </Admin>
  );
}

export default App;