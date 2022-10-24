export const parseErrorMessage = (e: any) => {
  try {
    if (e.response.status) {
      return e.response.data.message
    } else {
      return e.toString()
    }
  } catch (e) {
    console.error(e)
    return "알 수 없는 에러입니다.(메시지 해석 불가)"
  }
}
