use rand::Rng;

#[derive(Copy, Clone)]
struct Proceso {
    nombre: char,
    llegada: u32,
    duracion: u32
}

fn main() {
    const TICKETSTOTALES : usize = 120;
    let mut procesos : Vec<Proceso> = Vec::new();
    let mut tickets : Vec<char> = Vec::new();
    let mut ticks : Vec<u32> = Vec::new();
    let mut planificacion = String::from("");
    let mut rng = rand::thread_rng();
    let mut aux : u32;
    let n: u32 = rng.gen_range(5..8);
    let c: char = 'A';

    for _i in 1..n+1 {
        ticks.push(0);
    }

    let mut proceso_tmp = Proceso {
        nombre: char::from_u32(c as u32 - 1).unwrap_or(c),
        llegada: 0,
        duracion: 0
    };

    for number in 1..n+1 {
        proceso_tmp.nombre = char::from_u32(proceso_tmp.nombre as u32 + 1).unwrap_or(proceso_tmp.nombre);
        if proceso_tmp.nombre == 'A' {
            proceso_tmp.llegada = 0;
        } else {
            proceso_tmp.llegada = rng.gen_range(0..(10*(number)));
        }
        proceso_tmp.duracion = rng.gen_range(4..10);
        procesos.push(proceso_tmp);
    }

    imprimir_lista_procesos(procesos);

    println!("\nReparticion de tickets");

    for i in 0..TICKETSTOTALES {
        aux = rng.gen_range(0..n);
        tickets.push(char::from_u32(c as u32 + aux).unwrap_or(c));

        println!("No. de ticket: {0}",i+1);
        println!("Proceso: {0}", tickets[i]);
    }

    let mut aux2 : usize;

    for _i in 0..TICKETSTOTALES {
        aux2 = rng.gen_range(0..TICKETSTOTALES);
        planificacion.push(tickets[aux2]);
    }

    println!("\nPlanificacion:");
    println!{"{planificacion}"};

    println!("\nTabla de ejecucion:");

}

fn imprimir_lista_procesos(procesos: Vec<Proceso>) {
    println!("Lista de procesos:");
    println!("Proceso   Duracion   Llegada");
    for p in procesos.iter() {
        println!("{0}\t  {1}\t     {2}", p.nombre,p.duracion,p.llegada);
    }
}
