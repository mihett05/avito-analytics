import { combineDataProviders } from 'react-admin';

import { restProvider } from './rest';
import { priceProvider } from './prices';

export const dataProvider = combineDataProviders((resource) => {
  switch (resource) {
    case 'price':
      return priceProvider;
    default:
      return restProvider;
  }
});
