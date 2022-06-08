const reinforceStart = document.querySelector('#reinforceStart')
const weapon = document.querySelector('#workshop')
reinforceStart.addEventListener('click', function (event) {    
    const explanation = document.querySelector('#explanation')
    explanation.style.display = "none"
    weapon.style.display = "flex"
})
let stack = 1
const reinforceButton = document.querySelector('#reinforceButton')
const weaponImage = document.querySelector('#weaponImage')
const cardBody = document.querySelector('.card-body')
const backToStart = document.querySelector('#homeButton')
backToStart.addEventListener('click', function (event){
    window.location.reload()
})

reinforceButton.addEventListener('click', function (event) {
    event.preventDefault()
    console.log(event.target.data)    
    console.log(stack);
    stack += 1
    if (stack > 7){
        stack = 7 
        window.alert('최대 강화단계입니다. 축하합니다!')    
                
        

    }else {
        const randomNum = Math.floor(Math.random() * 7)
        console.log(randomNum);
        if (randomNum < stack* 0.3){
            window.alert('강화가 실패하였습니다 처음단계로 돌아갑니다!')
            stack = 1
        }       

        weaponImage.src = `./images/${stack}.png`
               

    }
})