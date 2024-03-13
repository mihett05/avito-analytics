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

const handlePriceResponse = (response: PriceResponse[]) =>
  response.map(
    ({ category_id, location_id, matrix_id, price }: PriceResponse): Price => ({
      location_id,
      category_id,
      matrix_id,
      price,
      id: getId({ category_id, location_id, matrix_id }),
    }),
  );

export const priceProvider: DataProvider = {
  getList: async (resource, params): Promise<GetListResult<Price>> => {
    const response = await api.get<PriceResponse[]>('/price');
    return {
      data: handlePriceResponse(response.data),
      total: response.headers['X-Total-Count'],
    };
  },
  getManyReference: async (resource, params) => {
    const { page, perPage } = params.pagination;
    const response = await api.get<PriceResponse[]>(
      `/price/${params.id}?_end=${perPage * page}&_start=${perPage * (page - 1)}`,
    );
    return {
      data: handlePriceResponse(response.data),
      total: response.headers['X-Total-Count'],
    };
  },
};
