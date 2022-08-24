export const dataChange = () => {
  const yyyyMMdd = (value) => {
    if(value == "") return ''
  
    const js_date = new Date(value)
  
    const year = js_date.getFullYear()
    let month = js_date.getMonth() + 1
    let day = js_date.getDate()
  
    if (month < 10) {
      month =  '0' + month
    }
  
    if (day < 10) {
      day = '0' + day
    }
  
    return year + '.' + month + '.' + day
  }

  const howNow = (value) => {
    if (value == "") return ''

    const nowTime = new Date()
    const createTime = new Date(value)

    const diffTime = (nowTime.getTime() - createTime) / (1000)

    if (diffTime < 60) {
      return Math.floor(diffTime + 1) + '초 전'
    } else if (diffTime < 3600) {
      return Math.floor(diffTime / 60) + '분 전'
    } else if (diffTime < 86400 ) {
      return Math.floor(diffTime / 3600) + '시간 전'
    } else if (diffTime < 604800) {
      return Math.floor(diffTime / 86400) + '일 전'
    } else {
      yyyyMMdd(value)
    }
  }

  return {
    yyyyMMdd,
    howNow
  }
}