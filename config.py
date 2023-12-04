dev=False
skill_shift=True #  False
spray_button= "1!"
tap_button=""# "2@"
x=2560
y=1440
#x=1920
#y=1080
guns_mapping={
('q', 'h'): ("akm" ,{"default":[(0.7, 0.032, 7),(2, 0.032, 10),(1.4, 0.03, 10)]}),
('q', 'j'): ("mk47 mutant" ,{"special":[(0.3,0.033, 7),(1, 0.03, 12),(0.8, 0.03, 12),(0.4, 0.029, 11)]}),
('q', 'k'): ("groza" ,{"default":[(0.9, 0.031, 6),(1.5, 0.028, 8),(0.8, 0.029, 8)]}),
('e', 'h'): ("beryl",{"default":[(0.3, 0.03, 8),(0.7, 0.026, 10),(1, 0.027, 13),(1.7, 0.0245, 13),(0.7, 0.024, 13)]}),
('3', 'h'): ("ace" ,{"default":[(0.4, 0.03, 6),(0.4, 0.027, 9),(0.3, 0.03, 13),(0.7, 0.03, 14),(1, 0.028, 14),(1.3, 0.029, 14)]}),
('4', 'h'): ("aug" ,{"default":[(0.4, 0.031, 6),(0.4, 0.027, 9),(0.3, 0.031, 13),(0.7, 0.03, 14),(2.3, 0.03, 14)]}),
('4', 'k'): ("mini 14" ,{"special":[(0.3, 0.03, 5),(0.5, 0.027, 11),(1.6, 0.029, 11),(1, 0.03, 11)]}),
('4', 'j'): ("m16a4" ,{"special":[(0.4, 0.029, 5),(0.3, 0.029, 9),(0.4, 0.029, 9),(0.3, 0.029, 9), (2, 0.031, 9)]}),
('5', 'h'): ("m416" ,{"default":[(0.4, 0.026, 5),(0.6, 0.029, 9),(1, 0.0255, 9),(1.6, 0.027, 10)]}),
('5', 'j'): ("thompson",{"default":[(0.4, 0.03,4),(0.4, 0.03,7),(0.4, 0.03,9),(6, 0.03,10)]}),
('5', 'k'): ("bizon",{"default":[(0.4, 0.045,5),(0.5, 0.04,7),(0.5, 0.043,7),(0.6, 0.045,7),(2.2, 0.042,6),(0.3, 0.045,6)]}),
('6', 'h'): ("scar-l",{"default":[(0.5, 0.03, 4),(0.3, 0.027, 5),(0.3, 0.028, 6),(0.3, 0.028, 7),(2.5, 0.03, 8)]}),
('6', 'j'): ("o12",{"special":[(3.8, 0.03,6)]}),
('6', 'k'): ("ump",{"default":[(0.5, 0.03,4),(0.3, 0.03,6),(0.4, 0.03,6),(0.3, 0.03,6),(1.8, 0.03,7)]}),
('7', 'h'): ("qbz" ,{"default":[(0.6, 0.032, 5),(0.3, 0.032, 7),(0.4, 0.031, 9),(0.3, 0.031, 9),(2.3, 0.032, 10)]}),
('7', 'j'): ("mg3" ,{"default":[(0.5, 0.03,2),(0.6, 0.03,3),(5.6, 0.03,4)]}),
('7', 'k'): ("mp9" ,{"default":[(0.4, 0.023,3),(0.5, 0.022,4),(0.4, 0.027,3),(1.1, 0.024,2)]}),
('8', 'h'): ("g36c" ,{"default":[(0.4, 0.032, 5),(0.3, 0.031, 7),(0.4, 0.03, 8),(0.3, 0.031, 9),(2.4, 0.031, 10)]}),
('8', 'j'): ("mp5k" ,{"default":[(0.3, 0.029, 5),(0.4, 0.03,9),(0.9, 0.031,9),(0.6, 0.03, 8),(0.5, 0.029, 8)]}),
('8', 'k'): ("p90" ,{"default":[(0.4, 0.09,12),(0.5, 0.09,18),(2.2, 0.09,9)]}),
('9', 'h'): ("k2", {"default":[(0.5, 0.032, 6),(0.3, 0.032, 8),(0.4, 0.031, 9),(0.3, 0.031, 9),(2.1, 0.031, 9)]}),
('9', 'j'): ("dp-28" ,{"default":[(0.5, 0.035, 4),(0.5, 0.029, 5), (0.5, 0.021, 5), (2.5, 0.0145, 4)]}),
('9', 'k'): ("m249" ,{"default":[(0.3, 0.042, 5), (0.6, 0.025, 6), (0.5, 0.042, 6), (0.4, 0.067, 6), (1.8, 0.057, 7), (8.4, 0.052, 7)]}),
('0', 'h'): ("famas" ,{"default":[(0.4, 0.03, 4),(0.4, 0.03, 8),(1.2, 0.03, 9)]}),
('0', 'j'): ("vector" ,{"default":[(0.4, 0.03, 5),(0.5, 0.026, 8),(1.3, 0.027, 11)]}),
('0', 'k'): ("micro uzi" ,{"default":[(0.4, 0.027,3),(0.6, 0.026,9),(0.8, 0.027, 12)]}),
('b', 'k'): ("battlebit_m4" ,{"special":[(0.1, 0.016, 16),(1, 0.017, 10),(5, 0.019, 10)]}),
}
snipers_mapping={
('p', '0'): ("sniper lv0",{"dmr": [(0.1,0.005,3),(0.05,0.01)]}),
('p', '1'): ("sniper lv1",{"dmr": [(0.1,0.005,5),(0.05,0.01,-2)]}),
('p', '2'): ("sniper lv2",{"dmr": [(0.1,0.005,7),(0.05,0.01,-6)]}),
('p', '3'): ("sniper lv3",{"dmr": [(0.1,0.005,10),(0.05,0.01,-10)]}),
('p', '4'): ("sniper lv4",{"dmr": [(0.1,0.005,13),(0.05,0.01,-13)]}),
('p', '5'): ("sniper lv5",{"dmr": [(0.1,0.005,14),(0.05,0.01,-15)]}), 
('p', '6'): ("sniper lv6",{"dmr": [(0.1,0.005,16),(0.05,0.01,-19)]}),
('p', '7'): ("sniper lv7",{"dmr": [(0.1,0.005,18),(0.05,0.01,-22)]}),
('p', '8'): ("sniper lv8",{"dmr": [(0.1,0.005,20),(0.05,0.01,-25)]}),
('p', '9'): ("sniper lv9",{"dmr": [(0.1,0.005,22),(0.05,0.01,-29)]}),
('u', '3'): ("ace x3 alter",{"default":[(0.6, 0.03,20),(0.3, 0.03,30),(0.4, 0.03,29),(0.3, 0.03,32),(1.5, 0.03,34),(0.5, 0.03,35)]}),
('u', '4'): ("aug x3 alter",{"default":[(0.4, 0.02,12),(0.3, 0.02,18),(0.4, 0.02,24),(0.3, 0.02,25),(2, 0.02,28)]}),
('u', '5'): ("m416 x3 alter",{"default":[(0.5, 0.03,16),(0.4, 0.03,23),(0.6, 0.03,25),(0.4, 0.03,26),(0.8, 0.03,29),(0.8, 0.03,29)]}),
('u', '6'): ("scar-l x3 alter",{"default":[(0.5, 0.03,13),(0.6, 0.03,21),(0.4, 0.03,23),(0.5, 0.03,24),(1, 0.03,25),(1, 0.03,25)]}),
('u', '7'): ("qbz x3 alter",{"default":[(0.5, 0.03,14),(0.4, 0.03,22),(0.4, 0.03,28),(0.4, 0.03,28),(2.1, 0.03,30)]}),
('u', '8'): ("g36c x3 alter",{"default":[(0.5, 0.03,15),(0.3, 0.03,21),(0.4, 0.03,27),(0.3, 0.03,29),(1.7, 0.03,30),(0.4, 0.03,29)]}),
}
coordinates ={"default":[(0.3, 0.03, 8),(0.7, 0.026, 10),(1, 0.027, 13),(1.7, 0.0245, 13),(0.7, 0.024, 13)]}
sniper_coordinates =  {"default": [(0.02,0.001,5)]}