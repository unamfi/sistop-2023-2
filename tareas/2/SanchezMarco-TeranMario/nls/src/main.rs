use std::fs;
use std::env;
use std::time::SystemTime;
use std::os::unix::fs::PermissionsExt;
use chrono::{DateTime, Local, Duration};

fn main() {
    //Read arguments from the command line
    let args: Vec<String> = env::args().collect();

    //Verify number of arguments
    if args.len() < 3 {
        panic!("not enough arguments");
    } else if args.len() > 3 {
        panic!("Too many arguments");
    } else {
        //Verify if is a directory
        let directory = fs::metadata(String::from(&args[1])).unwrap();
        if !directory.is_dir() {
            panic!("Not a directory");
        } else {
            let dir_path = String::from(&args[1]);
            let days: i64 = (String::from(&args[2])).parse().unwrap();
            get_dir_files(dir_path, days);
        }
    }
}

fn get_dir_files(dir_path: String, days: i64) {
    //Read files from directory
    if let Ok(entries) = fs::read_dir(dir_path) {
        println!("Nombre\t\t\tModificacion\tModo\tTamanio");
        println!("==========================================================");
        for entry in entries {
            if let Ok(entry) = entry {
                let Ok(metadata) = entry.metadata() else {
                    panic!("Can't get metadata");
                };

                let Ok(modified) = metadata.modified() else {
                    panic!("Can't get last modification date");
                };
                let mod_date: DateTime<Local> = modified.clone().into();
                let sys_time = SystemTime::now();
                let sys_date: DateTime<Local> = sys_time.clone().into();
                let ref_date = sys_date - Duration::seconds(86400*days);
                
                if mod_date.gt(&ref_date) {
                    let date = format!("{}", mod_date.format("%Y-%m-%d %H:%M:%S"));
                    let Ok(filename) = (entry.file_name()).into_string() else {
                        panic!("Can't get file name");
                    };
                    let permissions = metadata.permissions().mode();
                    let size = metadata.len();
                    println!("{}\t\t{:?}\t{permissions}\t{size}", filename, date);
                } else {
                    continue;
                }
            }
        }
    }
}
