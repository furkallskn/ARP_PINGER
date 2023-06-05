import argparse
import scapy.all as scapy

class ARPPing():

	def __init__(self):
		print("ARPPingleme başlatıldı.")

	def kullanici_input(self):
		parser = argparse.ArgumentParser()

		parser.add_argument('-i', '--ipaddress', type=str, help="ARP pingi yollanılacak ip range girin!!!")
		args = parser.parse_args()
		print(args.ipaddress)

		if args.ipaddress != None:
			return args
		else:
			print("Enter ip range!")


	def arp_calistir(self,ip):

		arp_request_packet = scapy.ARP(pdst=ip)

		broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

		combined_packet = broadcast_packet/arp_request_packet

		(answered_list, unanswered_list) = scapy.srp(combined_packet,timeout=1)

		answered_list.summary()

if __name__ == "__main__":
	arp_ping = ARPPing()
	ip_range = arp_ping.kullanici_input()
	arp_ping.arp_calistir(ip_range.ipaddress)
