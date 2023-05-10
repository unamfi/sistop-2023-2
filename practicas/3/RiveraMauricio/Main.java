import java.util.*;

public class Main{
	static int[][]a;
	static int[][]b;
	static int[][]c;


	static class PracticaDoce extends Thread{

		int id=-1;

		public PracticaDoce(int id){
			this.id=id;
		}

		public void run(){
			int halfA=a.length/2;
			int halfB=a[0].length/2;

			if(id==0){
				for(int m=0; m<halfB; m++){
					for(int w=0; w<halfA; w++){
						c[m][w]=a[m][w]+b[m][w];
					}
				}
			}
			if(id==1){
				for(int n=0; n<halfB; n++){
					for(int x=c[n].length-1; x>=halfA; x--){
						c[n][x]=a[n][x]+b[n][x];
					}
				}
			}
			if(id==2){
				for(int k=c.length-1; k>=halfB; k--){
					for(int y=0; y<halfA; y++){
						c[k][y]=a[k][y]+b[k][y];
					}
				}
			}
			if(id==3){
				for(int l=c.length-1; l>=halfB; l--){
					for(int z=c[l].length-1; z>=halfA; z--){
						c[l][z]=a[l][z]+b[l][z];
					}
				}
			}
		}
	}

	public static void fillMatrix(){
		Scanner stdin=new Scanner(System.in);
		ArrayList<String> data= new ArrayList<>();
		while(stdin.hasNextLine()){
			data.add(stdin.nextLine());
			if(data.get(data.size()-1).equals("")){
				data.remove(data.size()-1);
				break;
			}
		}

		String[] aux= data.get(0).split(" ");

		int columnSize=aux.length;
		int rawSize=data.size();

		a=new int[rawSize][columnSize];
		b=new int[rawSize][columnSize];
		c=new int[rawSize][columnSize];	

		for(int i=0; i<data.size(); i++){
			for(int j=0; j<aux.length; j++){
				a[i][j]=Integer.parseInt(aux[j]);
			}
			if(i+1==data.size()){
				break;
			}
			aux=data.get(i+1).split(" ");
		}

		data.clear();

		while(stdin.hasNextLine()){
			data.add(stdin.nextLine());
		}
		for(int i=0; i<data.size(); i++){
			aux=data.get(i).split(" ");
			for(int j=0; j<aux.length; j++){
				b[i][j]=Integer.parseInt(aux[j]);
			}
		}
	}

	public static void printMatrix(int[][] matrix){
		for(int i=0; i<matrix.length; i++){
			for(int j=0; j<matrix[i].length; j++){
				System.out.print(matrix[i][j] + " ");
			}
			System.out.print("\n");
		}
	}

	public static void main(String[] args) {
		fillMatrix();
		new PracticaDoce(0).start();
		new PracticaDoce(1).start();
		new PracticaDoce(2).start();
		new PracticaDoce(3).start();


		printMatrix(c);
	}
}