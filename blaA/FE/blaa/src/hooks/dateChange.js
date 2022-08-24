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
  
    return year + '-' + month + '-' + day
  }

  return {
    yyyyMMdd
  }
}