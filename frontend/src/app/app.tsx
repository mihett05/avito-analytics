import React from 'react';
import { Admin, CustomRoutes, EditGuesser, Resource, ShowGuesser } from 'react-admin';
import { Route } from 'react-router-dom';

import { dataProvider } from '~/providers';
import { i18nProvider } from './i18n';

import StoragePage from '~/resources/storage';
import CustomLayout from '~/layout/layout';

import { LocationsEdit, LocationsList, LocationsShow } from '~/resources/locations';
import { CategoriesEdit, CategoriesList, CategoriesShow } from '~/resources/categories';
import { PricesList } from '~/resources/prices';
import { MatricesList } from '~/resources/matrices';

function App() {
  return (
    <Admin dataProvider={dataProvider} layout={CustomLayout} i18nProvider={i18nProvider}>
      <Resource name="location" list={LocationsList} edit={LocationsEdit} show={LocationsShow} />
      <Resource name="category" list={CategoriesList} edit={CategoriesEdit} show={CategoriesShow} />
      <Resource name="price" list={PricesList} edit={EditGuesser} show={ShowGuesser} />
      <Resource name="matrix" list={MatricesList} edit={EditGuesser} show={ShowGuesser} />
      <CustomRoutes>
        <Route path="/storage" element={<StoragePage />} />
      </CustomRoutes>
    </Admin>
  );
}

export default App;
