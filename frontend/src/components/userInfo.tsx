import { UserInfo } from 'features/users/userInfoTypes';

interface Props {
  userInfo?: any;
}

function UserInfoData({ userInfo }: Props) {
  console.log(userInfo)
  return (
    <>
      {userInfo.map((userInfo: UserInfo, index: number) => (
        <div>
          {userInfo.children}
        </div>
      ))}
    </>
  )
}

export default UserInfoData