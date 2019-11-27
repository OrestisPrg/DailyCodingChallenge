/*This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.*/

import java.util.Scanner;

public class SumFun {

  public int[] sumFun(int[] list, int k) {
    int[] res;
    for (int i=0; i<list.length; i++) {
      for (int j=0; j<list.length; i++) {
        if ((list[i] + list[j] == k) && (list[i] != list[j])) {
          res[0] = list[i];
          res[1] = list[j];
          return res;
        }
      }
    }
    return res;
  }

  public static void main(String args[]){
    Scanner in = new Scanner(System.in);
    System.out.println("Provide List: ");
    int[] list = in.nextLine();
    System.out.println("Provide k: ");
    int k = in.nextLine();

    int[] res = sumFun(list,k);
    System.out.println(res);

  }
}
