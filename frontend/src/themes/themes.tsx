import {
  RaThemeOptions,
  defaultLightTheme,
  defaultDarkTheme,
  nanoDarkTheme,
  nanoLightTheme,
  radiantDarkTheme,
  radiantLightTheme,
  houseDarkTheme,
  houseLightTheme,
} from 'react-admin';

import { softLightTheme, softDarkTheme } from './softTheme';

export type ThemeName =
    | 'soft'
    | 'default'
    | 'nano'
    | 'radiant'
    | 'house';

export interface Theme {
    name: ThemeName;
    light: RaThemeOptions;
    dark?: RaThemeOptions;
}

export const themes: Array<Theme> = [
    { name: 'soft', light: softLightTheme, dark: softDarkTheme },
    { name: 'default', light: defaultLightTheme, dark: defaultDarkTheme },
    { name: 'nano', light: nanoLightTheme, dark: nanoDarkTheme },
    { name: 'radiant', light: radiantLightTheme, dark: radiantDarkTheme },
    { name: 'house', light: houseLightTheme, dark: houseDarkTheme },
];