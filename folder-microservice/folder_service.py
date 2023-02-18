from folder_model import Folder

class FolderService:
    id_counter = 3
    folders = [
        Folder('#', "UNKNOWN", "CVs with an unknown folder id"),
        Folder('1', "CTU_032223", "CTU Summer 2022-2023"),
        Folder('2', "ABC", "Abc Company 1/2/2023")
    ]

    @classmethod
    def get_all_folders(cls):
        return cls.folders

    @classmethod
    def create_folder(cls, folder):
        folder.id = str(cls.id_counter)
        cls.id_counter += 1
        cls.folders.append(folder)

        return folder
