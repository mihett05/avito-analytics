import React from 'react';
import { Admin, CustomRoutes, EditGuesser, Resource, ShowGuesser } from 'react-admin';
import { Route } from 'react-router-dom';

import { dataProvider } from '~/providers';
import { i18nProvider } from './i18n';

import StoragePage from '~/resources/storage';
import CustomLayout from '~/layout/layout';

import { LocationsEdit, LocationsList, LocationsShow } from '~/resources/locations';
import { CategoriesEdit, CategoriesList, CategoriesShow } from '~/resources/categories';
import { MatricesList, MatrixCreate } from '~/resources/matrices';
import MatrixEdit from '~/resources/matrices/edit';

function App() {
  return (
    <Admin dataProvider={dataProvider} layout={CustomLayout} i18nProvider={i18nProvider}>
      <Resource
        name="matrix"
        list={MatricesList}
        edit={MatrixEdit}
        show={ShowGuesser}
        create={MatrixCreate}
      />
      <Resource name="location" list={LocationsList} edit={LocationsEdit} show={LocationsShow} />
      <Resource name="category" list={CategoriesList} edit={CategoriesEdit} show={CategoriesShow} />
      <CustomRoutes>
        <Route path="/storage" element={<StoragePage />} />
      </CustomRoutes>
    </Admin>
  );
}

export default App;
