import type { DataProvider, GetListResult } from 'react-admin';
import { Price } from '~/entities';
import { api } from '~/api/api';

type PriceResponse = Omit<Price, 'id'>;

const getId = ({
  category_id,
  location_id,
  matrix_id,
}: Pick<Price, 'category_id' | 'location_id' | 'matrix_id'>) =>
  `${location_id}-${category_id}-${matrix_id}`;

export const priceProvider: DataProvider = {
  getList: async (resource, params): Promise<GetListResult<Price>> => {
    const response = await api.get('/price');
    return {
      data: (response.data as PriceResponse[]).map(
        ({ category_id, location_id, matrix_id, price }: PriceResponse): Price => ({
          location_id,
          category_id,
          matrix_id,
          price,
          id: getId({ category_id, location_id, matrix_id }),
        }),
      ),
      total: response.headers['X-Total-Count'],
    };
  },
};
