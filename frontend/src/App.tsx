import { useRoutes } from 'react-router-dom';
import router from './router';

import LocalizationProvider from '@mui/x-date-pickers/LocalizationProvider';

import { CssBaseline } from '@mui/material';
import { ThemeProvider } from '@mui/material/styles';
import * as themes from 'theme/Themes';
import { useAppDistpatch, useAppSelector } from 'app/hooks';
import { useState } from 'react';
import GlobalAlert from 'utils/GlobalAlert';

function App() {
  // const count = useAppSelector((state) => state.counter.value)
  // const dispatch = useAppDistpatch()
  const content = useRoutes(router);
  const [isOpenAlert, setIsOpenAlert] = useState<boolean>(false);
  const [alertType, setAlertType] = useState<"success" | "error">("success");
  const [alertMessage, setAlertMessage] = useState<string>('');

  const onClickAlertCloseButton = () => setIsOpenAlert(false)

  const showAlert = (message: string, type: "success" | "error" = "success") => {
    setIsOpenAlert(true);
    setAlertType(type);
    setAlertMessage(message);
  }

  return (
    <ThemeProvider theme={themes.theme}>
      {/* <LocalizationProvider dateAdapter={AdapterDayjs}> */}
      <CssBaseline />
      {content}
      <GlobalAlert isOpen={isOpenAlert} type={alertType} message={alertMessage} onClickCloseButton={onClickAlertCloseButton} />
      {/* </LocalizationProvider> */}
    </ThemeProvider>
  );
}

export default App;
