export interface UserInfo {
  guid:string
  name: string
  gender:string
  age:number
  birthday:string
  email: string
  password: string
  passwordConfirm:string
}

export interface newUserInfo {
  firstName:string
  lastName: string
  gender:string
  age:number
  birthday:Date
  mailAddress: string
  password: string
}
