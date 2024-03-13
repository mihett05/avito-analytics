import polyglotI18nProvider from 'ra-i18n-polyglot';
import russianMessages from 'ra-language-russian';

const ru = {
  ...russianMessages,
  resources: {
    location: {
      name: 'Локации',
    },
    category: {
      name: 'Категории',
    },
    price: {
      name: 'Матрицы цен',
    },
  },
};

export const i18nProvider = polyglotI18nProvider(() => ru, 'ru');
