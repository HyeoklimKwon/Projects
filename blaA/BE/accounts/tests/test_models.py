from rest_framework.test import APITestCase
from accounts.models import User 
from django.urls import reverse
from rest_framework import status


class TestModel(APITestCase) :
    
    # 기본 유저 생성 
    def test_creates_user(self) :
        
        # 기본 유저 생성 
        user=User.objects.create_user(name='test',email='test@gmail.com',password='password',
                                        tel='01046509260',nickname='nickname',region='대전광역시 유성구 덕명동',category='음식점',is_alba=True)
        
        self.assertIsInstance(user,User) 
        # 기본 user가 staff가 아닌가? 
        self.assertFalse(user.is_staff)
        # 생성된 user의 email과 생성시 입력한 email이 일치하는가 
        self.assertEqual(user.email,'test@gmail.com') 
    
    # 슈퍼 유저 생성 
    def test_creates_super_user(self) :
        
        # 슈퍼 유저 생성 
        user=User.objects.create_superuser(name='test',email='test@gmail.com',password='password',
                                        tel='01046509260',nickname='nickname',region='대전광역시 유성구 덕명동',category='음식점',is_alba=True)
        
        # 생성된 이메일이 User model의 instance인가. 
        self.assertIsInstance(user,User) 
        # 생성된 객체가 staff가 맞는가 ? 
        self.assertTrue(user.is_staff) 
        # 생성된 user의 email과 생성시 입력한 email이 일치하는가 
        self.assertEqual(user.email,'test@gmail.com') 

    #email 미입력 오류 테스트 
    def test_raises_error_when_no_email_is_supplied(self) :
        self.assertRaises(ValueError,User.objects.create_superuser, name='test',email='',password='password',tel='01046509260',nickname='nickname',region='대전광역시 유성구 덕명동',category='음식점',is_alba=True)
        self.assertRaisesMessage(ValueError,'The Email must be set')

    #username 미입력 오류 테스트
    def test_raises_error_when_no_username_is_supplied(self) :
        self.assertRaises(ValueError,User.objects.create_superuser, name='',email='test@gmail.com',password='password',tel='01046509260',nickname='nickname',region='대전광역시 유성구 덕명동',category='음식점',is_alba=True)
        self.assertRaisesMessage(ValueError,'The name must be set')
    
    
    def test_raises_error_with_message_when_no_username_is_supplied(self) :
        with self.assertRaisesMessage(ValueError,'The name must be set') :
            User.objects.create_superuser(name='',email='test@gmail.com',password='password123!@#')
            
    def test_raises_error_when_no_email_is_supplied2(self) :
        #print('test')
        self.assertRaises(ValueError,User.objects.create_superuser, username="test",email='',password='password123!@#')
    
class SignupAPITestCase(APITestCase) :
    def test_signup(self) :
        response = self.client.post(reverse("accounts:signup"),
        {'name':'test','email':'test@gmail.com','password':'password','tel':'01046509260',
        'nickname':'nickname','region':'대전광역시 유성구 덕명동','category':'음식점','is_alba':True})
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    def test_signup_no_email_is_supplied(self) :
        response = self.client.post(reverse("accounts:signup"),
        {'name':'test','email':'','password':'password','tel':'01046509260',
        'nickname':'nickname','region':'대전광역시 유성구 덕명동','category':'음식점','is_alba':True})
        #print(response.data)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
    

        