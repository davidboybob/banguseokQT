import { Alert, Snackbar } from "@mui/material";
import { createContext } from "react";


export const ShowAlert = createContext<(message: string, type: "success" | "error") => void>(() => { })

interface Props {
  isOpen: boolean
  type: "success" | "error"
  message: string
  onClickCloseButton: () => void
}

export default function GlobalAlert(props: Props) {
  return <Snackbar
    open={props.isOpen}
    autoHideDuration={6000}
    onClose={props.onClickCloseButton}>
    <Alert onClose={props.onClickCloseButton} severity={props.type} sx={{ width: '100%' }}>
      {props.message}
    </Alert>
  </Snackbar>
}


