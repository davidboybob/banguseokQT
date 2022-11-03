import * as React from 'react';
import { useContext, useState } from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import { ShowAlert } from 'utils/GlobalAlert';
import { parseErrorMessage } from 'utils/Error';
import { client } from 'api/client';
import { signInReqDto } from 'utils/dto/auth_dto';

function Copyright(props: any) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {'Copyright © '}
      <Link color="inherit" href="https://mui.com/">
        Mooksang Univ
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

export default function SignBaseLayout() {
  const showAlert = useContext(ShowAlert)

  const [currentSignInReqDto, setCurrentSignInReqDto] = useState<signInReqDto>()

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    try {
      const res = await client.post('/auth/login', currentSignInReqDto)
      // console.log(res.data)
    } catch (e) {
      console.log(e)
      showAlert(parseErrorMessage(e), "error")
    }
  };

  const onChangeEmail = (event: React.ChangeEvent<HTMLInputElement>) =>
    setCurrentSignInReqDto({ ...currentSignInReqDto!, email: event.target.value })

  const onChangePassword = (event: React.ChangeEvent<HTMLInputElement>) =>
    setCurrentSignInReqDto({ ...currentSignInReqDto!, password: event.target.value })

  return (
    <Grid container component="main" sx={{ height: '100vh' }}>
      <Grid
        item
        mobile={false}
        tablet={4}
        laptop={7}
        sx={{
          backgroundImage: 'url(https://source.unsplash.com/random)',
          backgroundRepeat: 'no-repeat',
          backgroundColor: (t) =>
            t.palette.mode === 'light' ? t.palette.grey[50] : t.palette.grey[900],
          backgroundSize: 'cover',
          backgroundPosition: 'center',
        }}
      />
      <Grid item mobile={12} tablet={8} laptop={5} component={Paper} elevation={6} square>
        <Box
          sx={{
            my: 8,
            mx: 4,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign in
          </Typography>
          <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 1 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              id="email"
              label="Email Address"
              name="email"
              autoComplete="email"
              onChange={onChangeEmail}
              value={currentSignInReqDto?.email ?? ""}
              autoFocus
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              onChange={onChangePassword}
              value={currentSignInReqDto?.password ?? ""}
              autoComplete="current-password"
            />
            <FormControlLabel
              control={<Checkbox value="remember" color="primary" />}
              label="Remember me"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Sign In
            </Button>
            <Grid container>
              <Grid item mobile>
                <Link href="#" variant="body2">
                  Forgot password?
                </Link>
              </Grid>
              <Grid item>
                <Link href="/signup" variant="body2">
                  {"Don't have an account? Sign Up"}
                </Link>
              </Grid>
            </Grid>
            <Copyright sx={{ mt: 5 }} />
          </Box>
        </Box>
      </Grid>
    </Grid>
  );
}