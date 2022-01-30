/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rent;

import java.util.Scanner;

/**
 *
 * @author User
 */
public class Rent {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        int x;
        
        int a;
        int a1=0;
        int a2=0;
        int a3=0;
        int a4=0;
        int a5=0;
        
        int b;
        int b1=0;
        int b2=0;
        int b3=0;
        int b4=0;
        int b5=0;
        
        String c;
        String c1;
        String c2;
        String c3;
        String c4;
        String c5;
        
        Scanner input = new Scanner(System.in);
        
        System.out.println("歡迎使用租車系統，請選擇租車or還車，租車請輸入1，還車請輸入2: ");
        x = input.nextInt();
        
        switch (x)
        {
            case 1:
        System.out.println("歡迎使用租車系統，請輸入會員編號: ");
        a = input.nextInt();
        switch (a)
        {
            case 1:
                System.out.println("請輸入欲借車輛編號: ");
                b = input.nextInt();
                switch (b)
                {
                    case 1:
                    ++b1;
                    System.out.println("租車成功");
                    break;
                    
                    case 2:
                    ++b2;
                    System.out.println("租車成功");
                    break;
                    
                    case 3:
                    ++b3;
                    System.out.println("租車成功");
                    break;
                    
                    case 4:
                    ++b4;
                    System.out.println("租車成功");
                    break;
                    
                    case 5:
                    ++b5;
                    System.out.println("租車成功");
                    break;
                    
                    default:
                        System.out.println("無此車輛");
                        break;
                }
                break;
                
            case 2:
                System.out.println("請輸入欲借車輛編號: ");
                b = input.nextInt();
                switch (b)
                {
                    case 1:
                    ++b1;
                    System.out.println("租車成功");
                    break;
                    
                    case 2:
                    ++b2;
                    System.out.println("租車成功");
                    break;
                    
                    case 3:
                    ++b3;
                    System.out.println("租車成功");
                    break;
                    
                    case 4:
                    ++b4;
                    System.out.println("租車成功");
                    break;
                    
                    case 5:
                    ++b5;
                    System.out.println("租車成功");
                    break;
                    
                    default:
                        System.out.println("無此車輛");
                        break;
                }
                break;
                
            case 3:
                System.out.println("請輸入欲借車輛編號: ");
                b = input.nextInt();
                switch (b)
                {
                    case 1:
                    ++b1;
                    System.out.println("租車成功");
                    break;
                    
                    case 2:
                    ++b2;
                    System.out.println("租車成功");
                    break;
                    
                    case 3:
                    ++b3;
                    System.out.println("租車成功");
                    break;
                    
                    case 4:
                    ++b4;
                    System.out.println("租車成功");
                    break;
                    
                    case 5:
                    ++b5;
                    System.out.println("租車成功");
                    break;
                    
                    default:
                        System.out.println("無此車輛");
                        break;
                }
                break;
                
            case 4:
                System.out.println("請輸入欲借車輛編號: ");
                b = input.nextInt();
                switch (b)
                {
                    case 1:
                    ++b1;
                    System.out.println("租車成功");
                    break;
                    
                    case 2:
                    ++b2;
                    System.out.println("租車成功");
                    break;
                    
                    case 3:
                    ++b3;
                    System.out.println("租車成功");
                    break;
                    
                    case 4:
                    ++b4;
                    System.out.println("租車成功");
                    break;
                    
                    case 5:
                    ++b5;
                    System.out.println("租車成功");
                    break;
                    
                    default:
                        System.out.println("無此車輛");
                        break;
                }
                break;
                
            case 5:
                System.out.println("請輸入欲借車輛編號: ");
                b = input.nextInt();
                switch (b)
                {
                    case 1:
                    ++b1;
                    System.out.println("租車成功");
                    break;
                    
                    case 2:
                    ++b2;
                    System.out.println("租車成功");
                    break;
                    
                    case 3:
                    ++b3;
                    System.out.println("租車成功");
                    break;
                    
                    case 4:
                    ++b4;
                    System.out.println("租車成功");
                    break;
                    
                    case 5:
                    ++b5;
                    System.out.println("租車成功");
                    break;
                    
                    default:
                        System.out.println("無此車輛");
                        break;
                }
                break;
                
            default:
                System.out.println("無此會員");
                break;
                
        }
        break;
        
            case 2:
            System.out.println("歡迎使用還車系統，請輸入會員編號: ");
            a = input.nextInt();
        switch (a)
        {
            case 1:
                System.out.println("請輸入欲還車輛編號: ");
                b = input.nextInt();
                switch (b)
                {
                    case 1:
                    --b1;
                    System.out.println("還車成功");
                    break;
                    
                    case 2:
                    --b2;
                    System.out.println("還車成功");
                    break;
                    
                    case 3:
                    --b3;
                    System.out.println("還車成功");
                    break;
                    
                    case 4:
                    --b4;
                    System.out.println("還車成功");
                    break;
                    
                    case 5:
                    --b5;
                    System.out.println("還車成功");
                    break;
                    
                    default:
                        System.out.println("無此車輛");
                        break;
                }
                break;
                
            case 2:
                System.out.println("請輸入欲還車輛編號: ");
                b = input.nextInt();
                switch (b)
                {
                    case 1:
                    --b1;
                    System.out.println("還車成功");
                    break;
                    
                    case 2:
                    --b2;
                    System.out.println("還車成功");
                    break;
                    
                    case 3:
                    --b3;
                    System.out.println("還車成功");
                    break;
                    
                    case 4:
                    --b4;
                    System.out.println("還車成功");
                    break;
                    
                    case 5:
                    --b5;
                    System.out.println("還車成功");
                    break;
                    
                    default:
                        System.out.println("無此車輛");
                        break;
                }
                break;
                
                
            case 3:
                System.out.println("請輸入欲還車輛編號: ");
                b = input.nextInt();
                switch (b)
                {
                    case 1:
                    --b1;
                    System.out.println("還車成功");
                    break;
                    
                    case 2:
                    --b2;
                    System.out.println("還車成功");
                    break;
                    
                    case 3:
                    --b3;
                    System.out.println("還車成功");
                    break;
                    
                    case 4:
                    --b4;
                    System.out.println("還車成功");
                    break;
                    
                    case 5:
                    --b5;
                    System.out.println("還車成功");
                    break;
                    
                    default:
                        System.out.println("無此車輛");
                        break;
                }
                break;
                
                
            case 4:
                System.out.println("請輸入欲還車輛編號: ");
                b = input.nextInt();
                switch (b)
                {
                    case 1:
                    --b1;
                    System.out.println("還車成功");
                    break;
                    
                    case 2:
                    --b2;
                    System.out.println("還車成功");
                    break;
                    
                    case 3:
                    --b3;
                    System.out.println("還車成功");
                    break;
                    
                    case 4:
                    --b4;
                    System.out.println("還車成功");
                    break;
                    
                    case 5:
                    --b5;
                    System.out.println("還車成功");
                    break;
                    
                    default:
                        System.out.println("無此車輛");
                        break;
                }
                break;
                
                
            case 5:
                System.out.println("請輸入欲還車輛編號: ");
                b = input.nextInt();
                switch (b)
                {
                    case 1:
                    --b1;
                    System.out.println("還車成功");
                    break;
                    
                    case 2:
                    --b2;
                    System.out.println("還車成功");
                    break;
                    
                    case 3:
                    --b3;
                    System.out.println("還車成功");
                    break;
                    
                    case 4:
                    --b4;
                    System.out.println("還車成功");
                    break;
                    
                    case 5:
                    --b5;
                    System.out.println("還車成功");
                    break;
                    
                    default:
                        System.out.println("無此車輛");
                        break;
                }
                break;
                
            default:
                System.out.println("無此會員");
                break;
        }
    break;
        }
    }
    
}
