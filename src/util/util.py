def split_file_name(abs_path) :
    if not isinstance(abs_path, str) :
        raise ValueError("Argument must be string")
    
    slash_idx = abs_path.rfind("/")
    dot_idx   = abs_path.rfind(".")

    return abs_path[slash_idx + 1 : dot_idx]