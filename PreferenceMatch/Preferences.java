import java.lang.String;
import java.util.ArrayList;


class Preferences{

	ArrayList<Vertice> hombres;
	ArrayList<Vertice> mujeres;

	public static void main(String[] args) {

		Preferences main = new Preferences();
		ArrayList<Vertice> noHanPropuesto;

		main.hombres = new ArrayList<Vertice>();
		main.hombres.add(new Vertice("Alan", null));
		main.hombres.add(new Vertice("Johor", null));
		main.hombres.add(new Vertice("David", null));

		main.mujeres.add(new Vertice("Edith", null));
		main.mujeres.add(new Vertice("Lea", null));
		main.mujeres.add(new Vertice("Nati", null));

		noHanPropuesto = main.getFaltantesDeProponer();
		while(noHanPropuesto.size()!=0){

			Vertice hombre = noHanPropuesto.get(0);
			Vertice w = hombre.porProponer.get(0);

			if( w.casado == null ){
				w.casado = hombre;
				hombre.casado = w;
			}
			else{
				Vertice m = w.casado;
				if(w.preferencia.indexOf(hombre) > w.preferencia.indexOf(m)){
					m.casado = null;
					w.casado = hombre;
					hombre.casado = w;
				}
			}

		}

	}

	private ArrayList<Vertice> getFaltantesDeProponer(){

		ArrayList<Vertice> resultado = new ArrayList<Vertice>();
		for(Vertice element:hombres){
			if(element.porProponer.size()>0){
				resultado.add(element);
			}
		}
		return resultado;

	}

}

class Vertice{

	String nombre;
	Vertice casado;
	ArrayList<Vertice> preferencia 	= new ArrayList<Vertice>();
	public ArrayList<Vertice> porProponer;

	public Vertice(String nombre, Vertice casado){
		this.nombre = nombre;
		this.casado = casado;
	}

	public void setPreferencia(ArrayList<Vertice> preferencia){
		this.preferencia = preferencia;
		this.porProponer = preferencia;
	}

	public void setSoltero(){
		this.casado = null;
		this.porProponer = preferencia;
	}

}