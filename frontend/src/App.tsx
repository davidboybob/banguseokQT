import { useRoutes } from 'react-router-dom';
import router from './router';

import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';

import LocalizationProvider from '@mui/x-date-pickers/LocalizationProvider';

import { CssBaseline } from '@mui/material';
import { ThemeProvider } from '@mui/material/styles';
import * as themes from 'theme/Themes';
import { useAppDistpatch, useAppSelector } from 'app/hooks';

function App() {
  // const count = useAppSelector((state) => state.counter.value)
  // const dispatch = useAppDistpatch()
  const content = useRoutes(router);

  return (
    <ThemeProvider theme={themes.theme}>
      {/* <LocalizationProvider dateAdapter={AdapterDayjs}> */}
      <CssBaseline />
      {content}
      {/* </LocalizationProvider> */}
    </ThemeProvider>
  );
}

export default App;
