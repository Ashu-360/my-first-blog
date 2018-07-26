from django.db import models
from django.utils import timezone

VEHICLE_TYPE = (
    ('car', 'Car'),
    ('bike', 'Bike'),
)


class Slot(models.Model):
    slot_no = models.IntegerField()
    # floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        self.slot_no


class Floor(models.Model):
    floor_no = models.IntegerField(unique=True)
    # no_of_slots = models.IntegerField(max_length=10)
    floor_name  = models.CharField(max_length=50, null=True, blank=True)
    slots = models.ManyToManyField(Slot)
    # slot_no = models.ForeignKey(Slot.slot_no, on_delete=models.CASCADE)

    def __str__(self):
        return self.floor_no


class VehicleInfo(models.Model):
    vehicle_type = models.CharField(max_length=15, choices=VEHICLE_TYPE)
    vehicle_no = models.TextField(max_length=30, unique=True, blank=False)
    owner_m_no = models.CharField(max_length=15)
    # floor_no = models.ForeignKey(Floor, on_delete= models.CASCADE)
    slot_no = models.ForeignKey(Slot, on_delete= models.CASCADE)

    def __str__(self):
        return self.vehicle_no


class Slip(models.Model):
    v_no = models.ForeignKey(VehicleInfo,related_name="slip_veh_no", on_delete=models.CASCADE)
    v_type = models.ForeignKey(VehicleInfo,related_name="slip_veh_type", on_delete=models.CASCADE)
    # f_no = models.ForeignKey(VehicleInfo.floor_no,on_delete=models.CASCADE)
    s_no = models.ForeignKey(Slot, on_delete=models.CASCADE)
    entry_time = models.DateTimeField(default=timezone.now )
    exit_time = models.DateTimeField(default=None)

    def __str__(self):
        self.v_no









