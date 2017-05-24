class Solution { 
	public int solution(int[] A) {
		double sum = 0;
		for (int i=0; i< A.length; i++)
			sum += A[i];

		double res = 0.5*(A.length+1)*(A.length+2) - sum;
		return (int)res;

	}
}

public class PermMissingElem {
	public static void main(String [] args) {
		int[] array = {1,2,3,4,5,6,7,8,9};
		Solution obj = new Solution();
		System.out.printf("result: %d", obj.solution(array));	
	}
}