{
  description = "end-4 Hyprland dotfiles with NixOS home-manager module";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    quickshell = {
      url = "git+https://git.outfoxxed.me/outfoxxed/quickshell";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    nur = {
      url = "github:nix-community/NUR";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, quickshell, nur, ... }: {
    homeManagerModules.default = { config, lib, pkgs, ... }:
      (import ./nix/home-module.nix) {
        inherit config lib pkgs;
        inputs = { inherit quickshell nur; dotfiles = self; };
      };
    homeManagerModules.illogical-flake = self.homeManagerModules.default;
  };
}
