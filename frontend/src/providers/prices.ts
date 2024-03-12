import type { DataProvider, GetListResult } from 'react-admin';
import axios from 'axios';
import { Price } from '~/entities';

const base = axios.create({
  baseURL: import.meta.env.VITE_API_BASE,
});

type PriceResponse = Omit<Price, 'id'>;

const getId = ({
  category_id,
  location_id,
  matrix_id,
}: Pick<Price, 'category_id' | 'location_id' | 'matrix_id'>) =>
  `${location_id}-${category_id}-${matrix_id}`;

export const priceProvider: DataProvider = {
  getList: async (resource, params): Promise<GetListResult<Price>> => {
    const response = await base.get('/price');
    console.log(response);
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