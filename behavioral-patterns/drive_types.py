from abc import ABC, abstractmethod

class DriveType(ABC):
    @abstractmethod
    def add_drive_type(self):
        pass

class AllWheelDrive(DriveType):
    def add_drive_type(self):
        print("- All-wheel drive added")

class FrontWheelDrive(DriveType):
    def add_drive_type(self):
        print("- Front wheel drive added")

class BackWheelDrive(DriveType):
    def add_drive_type(self):
        print("- Back wheel drive added")