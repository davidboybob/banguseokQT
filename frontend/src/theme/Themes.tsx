import { createTheme } from '@mui/material/styles';
import { yellow } from '@mui/material/colors';


declare module '@mui/material/styles' {
  interface Theme {
    color: {
      primary: {
        main: string;
      }
    }
  }

  interface BreakpointOverrides {
    xs: false; // removes the `xs` breakpoint
    sm: false;
    md: false;
    lg: false;
    xl: false;
    mobile: true; // adds the `mobile` breakpoint
    tablet: true;
    laptop: true;
    desktop: true;
  }
}

export const theme = createTheme({
  typography: {
    fontFamily: ["NanumBarunGothic", "NanumBarunGothicBold", "Roboto"].join(','),
  },
  palette: {
    primary: {
      main: yellow[500],
    }
  },
  breakpoints: {
    values: {
      mobile: 0,
      tablet: 640,
      laptop: 1024,
      desktop: 1200,
    },
  },
})