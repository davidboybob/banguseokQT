import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import React, { useContext, useState } from 'react';
import { Checkbox, FormControlLabel } from '@mui/material';
import { ShowAlert } from 'utils/GlobalAlert';
import { parseErrorMessage } from 'utils/Error';
import { client } from 'api/client';

interface signUpReqDto {
  name: string,
  email: string,
  password: string,
}


export default function SignUpLayout() {
  const [currentSignUpReqDto, setCurrentSignUpReqDto] = useState<signUpReqDto>()
  const showAlert = useContext(ShowAlert)

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    try {
      client.post("")
    } catch (e) {
      showAlert(parseErrorMessage(e), "error")
    }

  }

  const onChangeName = (event: React.ChangeEvent<HTMLInputElement>) =>
    setCurrentSignUpReqDto({ ...currentSignUpReqDto!, name: event.target.value })
  const onChangeEmail = (event: React.ChangeEvent<HTMLInputElement>) =>
    setCurrentSignUpReqDto({ ...currentSignUpReqDto!, email: event.target.value })
  const onChangePassword = (event: React.ChangeEvent<HTMLInputElement>) =>
    setCurrentSignUpReqDto({ ...currentSignUpReqDto!, password: event.target.value })

  return (
    <Container component="main" maxWidth="desktop">
      <Box
        sx={{
          marginTop: 8,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          회원 가입
        </Typography>
        <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
          <Grid container spacing={2}>
            <Grid item mobile={12} tablet={12}>
              <TextField
                autoComplete="given-name"
                name="name"
                required
                fullWidth
                id="name"
                label="이름"
                onChange={onChangeName}
                value={currentSignUpReqDto?.name || ''}
                autoFocus
              />
            </Grid>
            <Grid item mobile={12}>
              <TextField
                required
                fullWidth
                id="email"
                label="이메일"
                name="email"
                onChange={onChangeEmail}
                value={currentSignUpReqDto?.email || ''}
                autoComplete="email"
              />
            </Grid>
            <Grid item mobile={12}>
              <TextField
                required
                fullWidth
                name="password"
                label="비밀번호"
                type="password"
                id="password"
                onChange={onChangePassword}
                value={currentSignUpReqDto?.password || ''}
                autoComplete="new-password"
              />
            </Grid>
            <Grid item mobile={12}>
              <FormControlLabel
                control={<Checkbox value="allowExtraEmails" color="primary" />}
                label="I want to receive inspiration, marketing promotions and updates via email."
              />
            </Grid>
          </Grid>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
          >
            가입하기
          </Button>
          <Grid container justifyContent="flex-end">
            <Grid item>
              <Link href="/login" variant="body2">
                Already have an account? Sign in
              </Link>
            </Grid>
          </Grid>
        </Box>
      </Box>
    </Container>
  );
}
